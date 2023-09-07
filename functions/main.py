# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`
from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore,credentials


cred = credentials.Certificate("./serviceAccountKey.json")
initialize_app(cred)

@https_fn.on_request()
def get_firestore_data(req: https_fn.Request) -> https_fn.Response:
    try:

        db = firestore.client()

        collection_ref = db.collection("partiesDetails")
        document_ref = collection_ref.document("rj")
        print(f"aasdfvfadsghasfdccv", document_ref)
        # Retrieve the document snapshot
        doc = document_ref.get()
        data = doc.to_dict()

        # Check if the document exists
        if data.exists:
            # Convert DocumentSnapshot to a Python dictionary
            #data = doc.to_dict()

            # Access specific fields within the data
            event_name = data.get("eventName")
            event_date = data.get("eventDate")

            # Print or process the data as needed
            print("Event Name:", event_name)
            print("Event Date:", event_date)

            return https_fn.Response(data)   # Return the data as a dictionary

        else:
            print("Document does not exist")
            return https_fn.Response(None)

        # events_ref = db.collection("partiesDetails").document("rudransh")
        # doc = events_ref.get()
        # print("hgjgvjvj" + str(doc))
        # return https_fn.Response(str(doc.to_dict()))

        # if doc.exists:
        #     return https_fn.Response("Document data exits")
        # else:
        #     return https_fn.Response("No such document!")

        # event_data=[]
        # docs = events_ref.stream()
        # for doc in docs:
        #     print(f"{doc.id} => {doc.to_dict()}")
        #     event_data.append(doc.to_dict())
        
        # return https_fn.Response(f"Message with ID {doc.id} added.")
        
        # return{"data":event_data},200
    
    except Exception as e:
        return {"error": str(e)},500




# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")