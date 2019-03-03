# Tweet Generator

This is a repo that randomly generates tweets using Markov models.

## [sample.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/sample.py)
*The above file demonstrates:*
1. how to random a word from a text by the possibility of how often they show up in the text.

## [python_quote.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/python_quote.py)
*The above file demonstrates:*
1. returns random word from array that contains words
2. returns the rearangment of users terminal input into a string (using Fisher-Yates shuffle)
3. returns reversed arrangment of users terminal input

## [dictionary_words.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/dictionary_words.py)
*The above file demonstrates:*
1. returns random sentence with n amount of words (from the terminal input) from the dictionary file on our computer
3. split words from a file into an array
4. returns a plain string to a sentence format with capital letter at the front and full stop at the end

## [histogram_word_count.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/histogram_word_count.py)
*The above file demonstrates:*
1. turns a text file to a list of words excluding punctuations
1. returns a histogram that displays the word and the number of times it appeared in a given text file (*dictionary, lists of lists, lists of tuples, list of counts*)
2. returns number of words that are unique in the text file
3. returns the amount of times a given word has appeared in the text file
4. returns the most frequent word used in the text file


## [cowsay.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/cowsay.py)
*The above file demonstrates*
1. a script that imitates cowsay
2. how to format strings with a given input


## [autocomplete.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/autocomplete.py)
*The above file demonstrates*
1. how to return complete words that start with a given letter or letter sequence


## [appArchitect](https://github.com/RinniSwift/Tweet-Generator/tree/master/AppArchitecture)
1. **[dictogram.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/dictogram.py)**
*class for creating a dictogram. (histogram which is implemented as a subclass of dict type)*
2. **[dictogram_test.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/dictogram_test.py)**
*test cases for the dictogram.*
3. **[listogram.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/listogram.py)**
*class for creating a listogram. (histogram which is implemented as a subclass of list type)*
4. **[listogram_test.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/listogram_test.py)**
*test cases for listogram.*
5. **[linked_list.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/linked_list.py)**
*class for creating a linked list.*
6. **[linked_list_test.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/linked_list_test.py)**
*test cases for lisnked list.*
3. **[hashtable.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/hashtable.py)**
*class for creating a hash table. (implements the linked list)*
4. **[hashtable_test.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/AppArchitecture/hashtable_test.py)**
*test cases for hash table.*


## virtualenv
*web environmental setup with virtualenv tool*
1. **[venv](https://github.com/RinniSwift/Tweet-Generator/tree/master/venv)**
2. **[procfile](https://github.com/RinniSwift/Tweet-Generator/blob/master/Procfile)**
*determining we want to use 4 worker threads in our flask app*
3. **[app.py](https://github.com/RinniSwift/Tweet-Generator/blob/master/app.py)**
*where heroku reads to display content on the web page*
4. **[requirements.txt](https://github.com/RinniSwift/Tweet-Generator/blob/master/requirements.txt)**
*app requirements*
5. **[runtime.txt](https://github.com/RinniSwift/Tweet-Generator/blob/master/runtime.txt)**
*indicates what python version to use*