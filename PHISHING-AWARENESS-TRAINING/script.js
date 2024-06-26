// Quiz questions data (example)
const quizQuestions = [
    {
        question: "What is phishing?",
        options: ["A fishing technique", "A type of cyber attack", "A social media platform"],
        answer: 1
    },
    {
        question: "Which of the following is a common phishing tactic?",
        options: ["Sending fake emails", "Calling directly on phone", "Sending SMS"],
        answer: 0
    },
    // Add more questions as needed
];

let currentQuestion = 0;
let score = 0;

function loadQuiz() {
    const quizElement = document.getElementById('quiz');
    const currentQuizQuestion = quizQuestions[currentQuestion];

    let optionsHtml = '';
    for (let i = 0; i < currentQuizQuestion.options.length; i++) {
        optionsHtml += `<input type="radio" name="quizOption" value="${i}"> ${currentQuizQuestion.options[i]} <br>`;
    }
    
    quizElement.innerHTML = `<h3>${currentQuizQuestion.question}</h3>${optionsHtml}`;
}

function submitQuiz() {
    const selectedOption = document.querySelector('input[name="quizOption"]:checked');
    
    if (!selectedOption) {
        alert("Please select an option.");
        return;
    }
    
    const answerIndex = parseInt(selectedOption.value);
    const correctAnswer = quizQuestions[currentQuestion].answer;
    
    if (answerIndex === correctAnswer) {
        score++;
    }
    
    currentQuestion++;
    
    if (currentQuestion < quizQuestions.length) {
        loadQuiz();
    } else {
        showQuizResults();
    }
}

function showQuizResults() {
    const quizResultsElement = document.getElementById('quizResults');
    quizResultsElement.innerHTML = `<h3>Quiz Results</h3>
                                    <p>Your score: ${score} out of ${quizQuestions.length}</p>`;
}

// Initialize quiz when page loads
window.onload = function() {
    loadQuiz();
};
