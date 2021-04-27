import string
import os

import tensorflow as tf
import numpy as np

from typing import Any

from keras_bert import load_vocabulary, load_trained_model_from_checkpoint, Tokenizer

from nltk.corpus import wordnet


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

CONFIG = "bert/bert_config/multi_cased_L-12_H-768_A-12/bert_config.json"
CHECKPOINT = "bert/bert_config/multi_cased_L-12_H-768_A-12/bert_model.ckpt"
VOCAB = "bert/bert_config/multi_cased_L-12_H-768_A-12/vocab.txt"


class BertSearch:
    def __init__(self, max_seq):
        self.max_seq = max_seq
        self.model = load_trained_model_from_checkpoint(CONFIG, CHECKPOINT, seq_len=self.max_seq)
        self.tokenizer = Tokenizer(load_vocabulary(VOCAB))

    def search(self, search_term: str) -> list or None:
        try:
            syn_check, syn_list = self.get_syn_list(search_term)
            if not syn_check:
                return syn_list

            indices, segments, tokens = self.get_tokens(search_term, syn_list)
            if indices is None or segments is None or tokens is None:
                return syn_list

            prediction = self.get_prediction(search_term, indices, segments)

            result = self.parse_results(search_term, tokens, prediction)
            return result
        except Exception as e:
            print(f"error searching for term {search_term}: {e}")
            return None

    def get_syn_list(self, term) -> (bool, list):
        try:
            term = term.translate(str.maketrans('', '', string.punctuation))
            synonym_set = self.create_synset(term)
            if not synonym_set:
                return False, [(term, 0.0)]

            synonyms = []
            for syn in synonym_set:
                for lemma in syn.lemmas():
                    synonyms.append(lemma.name())

            synset = set(synonyms)
            synset.add(term)
            syn_list = [synonym for synonym in synset if "_" not in synonym and "-" not in synonym]
            return True, syn_list
        except Exception as e:
            print(f"error creating syn_list for {term}: {e}")
            return False, [(term, 0.0)]

    def get_tokens(self, term, syn_list) -> (Any, Any, Any):
        try:
            text = " ".join(set(syn_list))

            tokens = self.tokenizer.tokenize(text)
            indices, segments = self.tokenizer.encode(first=text, max_len=self.max_seq)
            return indices, segments, tokens
        except Exception as e:
            print(f"error creating tokens for {term}: {e}")
            return None, None, None

    def get_prediction(self, term, indices, segments) -> np.ndarray or None:
        try:
            return self.model.predict([np.array([indices]), np.array([segments])])[0]
        except Exception as e:
            print(f"error predicting results for {term}: {e}")
            return None

    def parse_results(self, term, tokens, prediction) -> list or None:
        try:
            tok_list = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1:
                    curr = [tokens[i], [np.array(prediction[i].tolist())]]
                    next = [tokens[i + 1], [np.array(prediction[i + 1].tolist())]]
                    if next[0][:2] == "##":
                        while True:
                            if next[0][:2] == "##":
                                curr[0] += next[0][2:]
                                curr[1] += next[1]
                                i += 1
                                next = [tokens[i + 1], [np.array(prediction[i].tolist())]]
                            else:
                                break
                    else:
                        i += 1
                    if curr[0][:2] != "##":
                        tok_list.append(curr)
                else:
                    tok_list.append([tokens[-1], [np.array(prediction[-1].tolist())]])
                    i += 1

            sum_tok_list = []
            base_tuple = ()
            for token, arr_list in tok_list:
                if token == "[SEP]" or token == "[CLS]":
                    continue
                sum_list = sum(arr_list)
                # sum_list = np.mean(arr_list)
                sum_tok_list.append((token, sum_list))
                if token == term:
                    base_tuple = (token, sum_list)
            diff_tok_list = []
            for token, arr_list in sum_tok_list:
                diff_list = arr_list - base_tuple[1]
                diff_list = np.linalg.norm(diff_list)
                diff_tok_list.append((token, diff_list))
            sorted_toks = sorted(diff_tok_list, key=lambda x: x[1])
            exclusive_toks = []
            seen = set()
            for tok, val in sorted_toks:
                if tok not in seen:
                    exclusive_toks.append((tok, val))
                    seen.add(tok)

            return exclusive_toks

        except Exception as e:
            print(f"error parsing results for {term}: {e}")
            return None

    @staticmethod
    def create_synset(term) -> list or None:
        synonym_set = wordnet.synsets(term)
        if not synonym_set:
            ## word not recognized
            print("word not found")
            return None
        return synonym_set
