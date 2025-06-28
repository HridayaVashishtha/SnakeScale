// script.js

document.addEventListener('DOMContentLoaded', () => {
    const TIME_LIMIT = 60; // seconds
    let timeLeft = TIME_LIMIT;
    const timerElement = document.getElementById('time');
    const accuracyElement = document.getElementById('accuracy');
    const userInput = document.getElementById('userInput');
    const testText = document.getElementById('testText').innerText;

    // Start Countdown Timer
    const timer = setInterval(() => {
        timeLeft--;
        timerElement.innerText = timeLeft;
        if (timeLeft <= 0) {
            clearInterval(timer);
            // Submit the form automatically when time is up
            document.getElementById('typingForm').submit();
        }
    }, 1000);

    // Real-Time Accuracy Calculation
    userInput.addEventListener('input', () => {
        const inputText = userInput.value;
        let correct = 0;
        for (let i = 0; i < Math.min(inputText.length, testText.length); i++) {
            if (inputText[i] === testText[i]) {
                correct++;
            }
        }
        const accuracy = ((correct / testText.length) * 100).toFixed(2);
        accuracyElement.innerText = `Accuracy: ${accuracy}%`;
    });
});