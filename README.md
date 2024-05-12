# Workout Scheduler

## A simple website that uses OpenAI API to generate a workout schedule based on the available days.

### IMPORTANT: API key was disabled when repo set to public. Please paste your own OpenAI API key in app.py for it to work.

Demo: https://youtu.be/SiX1b3Pm6tA
 
This project allows users to select what days they are available, and calls OpenAI API with a prompt. It then displays the generated text that includes a workout schedule for the user.

The prompt used:
```
Create a full workout schedule and list out every excercise with sets and reps for the following days: {', '.join(days)}. 
Focus on weightlifting and account for fatigue.
Use workout splits such as push pull legs, full body, or upper/lower depending on the amount of days chosen.
```

### Technologies used
* Frontend: HTML, CSS, Javascript
* Backend: Python, Flask
