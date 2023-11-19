# Your utility functions here
def create_tf_serving_json(data):    
    return {'inputs': {name: data[name].tolist() for name in data.keys()} if isinstance(data, dict) else data.tolist()}