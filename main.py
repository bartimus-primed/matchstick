from lib.endpoints.endpoints import Endpoints

if __name__ == "__main__":
    auth_key = "TEST_AUTH"
    ping_endpoint = {
        "/v1/ping": {
            "methods": ["GET"]
            }
        }
    chain_endpoint = {
        "/v1/chain/:id?": {
            "methods": ["GET", "POST", "PUT", "DELETE"],
            }
        }
    agent_endpoint = {
        "/v1/agent/:name?": {
            "methods": ["GET", "PUT", "DELETE"],
        }
    }
    agent_facts_endpoint = {
        "v1/agent/:name/facts": {
            "methods": ["POST", "DELETE"]
        }
    }
    ttp_endpoint = {
        "/v1/ttp/:id?": {
            "methods": ["GET", "POST", "PUT", "DELETE"]
        }
    }
    plugin_endpoint = {
        "/v1/plugin/:name?": {
            "methods": ["GET"]
        }
    }
    payload_endpoint = {
        "/v1/payload": {
            "methods": ["GET", "PUT"]
        }
    }
    schedule_endpoint = {
        "/v1/schedule": {
            "methods": ["POST"]
        }
    }
    endpoints = Endpoints.new_endpoints("https://127.0.0.1:8888", [
        ping_endpoint,
        chain_endpoint,
        agent_endpoint,
        ttp_endpoint,
        plugin_endpoint,
        payload_endpoint,
        schedule_endpoint,
    ], auth_key)

    endpoints.test_endpoints()
    [x.fuzz() for x in endpoints]
