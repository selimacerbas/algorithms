import math
from collections import defaultdict

class MultinomialNB:
    def __init__(self, articles_per_tag, alpha=1.0):
        self.articles_per_tag = articles_per_tag
        self.tags = list(articles_per_tag.keys())
        self.alpha = alpha
        self.priors_per_tag = {}
        self.likelihood_per_word_per_tag = {}
        self.train()

    def train(self):
        # Compute prior probabilities: P(tag)
        tag_counts = {tag: len(self.articles_per_tag[tag]) for tag in self.tags}
        total_articles = sum(tag_counts.values())
        self.priors_per_tag = {tag: count / total_articles for tag, count in tag_counts.items()}

        # Compute likelihoods: P(word | tag)
        self.likelihood_per_word_per_tag = self.__get_word_likelihoods_per_tag()

    def predict(self, article):
        # Initialize posteriors with log-priors for numerical stability
        posteriors = {tag: math.log(prior) for tag, prior in self.priors_per_tag.items()}

        for word in article:
            for tag in self.tags:
                # Use log-likelihood, and default to small probability if word not seen
                likelihood = self.likelihood_per_word_per_tag.get(word, {}).get(tag, self.alpha / 1)
                posteriors[tag] += math.log(likelihood)

        return posteriors

    def __get_word_likelihoods_per_tag(self):
        word_frequencies = defaultdict(lambda: {tag: 0 for tag in self.tags})
        total_word_count = defaultdict(int)

        for tag in self.tags:
            for article in self.articles_per_tag[tag]:
                for word in article:
                    word_frequencies[word][tag] += 1
                    total_word_count[tag] += 1

        word_likelihoods = defaultdict(dict)
        for word, freq_map in word_frequencies.items():
            for tag in self.tags:
                # Apply Laplace smoothing
                word_likelihoods[word][tag] = (
                    freq_map[tag] + self.alpha
                ) / (total_word_count[tag] + self.alpha * len(word_frequencies))

        return word_likelihoods
