from flask import Flask
from flask import request
from flask import json

app = Flask(__name__)


# -- DO NOT EDIT
# sample end point for HTTP Get
@app.route("/")
def default():
    """
    default endpoint for this server, just for demo.

    :return: str
    """
    return "FIRST PROJECT - we have " + str(len(get_client_rates())) + " clients in total."


# sample data load function
# This is a temporary data file - when we get to know more about database and cloud storage
# we would not be using this kind of data storage.
def get_client_rates():
    """
    return all the client - rate pairs we have.

    :return: dict {id: {'rate':float}}
    """
    import pandas as pd
    df = pd.read_json("client_rate.json")
    return df.to_dict()
print(get_client_rates())
# -- DO NOT EDIT END


# -- TODO: Part 1 - add an endpoint to get rate by client id
# When query http://hostname/rate/client1 it would return the rate number for client1 - 0.2
@app.route("/rate/<client_id>")
def get_client_rate(client_id):
    """
    End point for getting rate for a client_id.

    :param client_id: str
    :return: http response
    """
    # How to get the actual rate from client_id?
    client_dict = get_client_rates()
    if client_id in client_dict:
        return str(client_dict[client_id]['rate'])
    return client_id + ' is not found'
# -- TODO END: Part 1


# -- TODO: Part 4 - add an endpoint to add more client and rates data
@app.route("/rate", methods=['POST'])
def upsert_client_rate():
    """
    End point for updating or inserting client rate values in the post param.

    :return: http response.
    """
    # We want to update if the client exist in the client_rate.json data
    # Or insert a new client-rate pair into client_rate.json data


    # After getting post request - how to update json file?
    json_dict = request.get_json()
    list_key = json_dict.keys()
    list_value = json_dict.values()
    update_client_rates(list_key[0], list_value[0])
    return request.get_json()

def update_client_rates(client_id, rate):
    """
    update or insert a client_id - rate pair.

    :param client_id: string, e.g. 'client1'
    :param rate: float, e.g. 0.1
    :return:
    """
    # check if exist
    # replace or add client rate
    # re-write the file
    client_dict = get_client_rates()
    if client_id in client_dict:
        client_dict[client_id]['rate'] = rate
    else:
        client_dict.append(client_id,{'rate':rate})
    id_rate_dict.to_json("client_rate.json")
# -- TODO END: Part 4


if __name__ == "__main__":
    app.run()
