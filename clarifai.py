from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='b6f19e737e634138bc13363521689bb6')

model = app.models.get('food-items-v1.0')

response = model.predict_by_url(url='https://cdn.daysoftheyear.com/wp-content/images/hot-dog-day2-e1437733838777-808x380.jpg')

print response