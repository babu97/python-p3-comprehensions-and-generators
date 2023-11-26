#!/usr/bin/env python3


def return_evens(num_list):
    even_numbers = [number for number in num_list if number % 2 == 0]
    return even_numbers


def make_exclamation(sentence_list):
    exclamatory_sentences = [sentence + "!" for sentence in sentence_list]
    return exclamatory_sentences

