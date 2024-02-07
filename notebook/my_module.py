import pickle


def load_bertopic_model(model_path):
    with open(model_path, "rb") as model_file:
        topic_model = pickle.load(model_file)
    return topic_model


def assign_topics_to_batch(texts, model_path):
    # Load the BERTopic model once for the batch
    topic_model = load_bertopic_model(model_path)

    # Process all texts in the batch
    batch_results = []
    for text in texts:
        topics, _ = topic_model.transform([text])
        if topics:
            batch_results.append(topics[0])
        else:
            batch_results.append(None)
    return batch_results


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]
