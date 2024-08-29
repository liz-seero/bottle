// utils.js

// A utility function to generate a unique ID
function generateUniqueId() {
    return 'id-' + Math.random().toString(36).substr(2, 9);
}

// A utility function to format dates
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
}

// A function to get a random integer within a range
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// A function to check if a string is a palindrome
function isPalindrome(str) {
    const cleanedStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    return cleanedStr === cleanedStr.split('').reverse().join('');
}

// Function to calculate the factorial of a number
function factorial(n) {
    if (n < 0) return undefined; // factorial of negative numbers is not defined
    return n <= 1 ? 1 : n * factorial(n - 1);
}

// Function to fetch data from an API and handle errors
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

// DOM Manipulation

// Function to create a new element with text content
function createElement(type, textContent) {
    const element = document.createElement(type);
    element.textContent = textContent;
    return element;
}

// Function to append a new item to a list
function appendToList(listId, itemText) {
    const list = document.getElementById(listId);
    if (list) {
        const listItem = createElement('li', itemText);
        list.appendChild(listItem);
    }
}

// Function to toggle a class on an element
function toggleClass(elementId, className) {
    const element = document.getElementById(elementId);
    if (element) {
        element.classList.toggle(className);
    }
}

// Event Handling

// Function to handle button clicks
function handleButtonClick(event) {
    const button = event.target;
    alert('Button clicked: ' + button.textContent);
}

// Add event listeners to buttons with class 'my-button'
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.my-button');
    buttons.forEach(button => {
        button.addEventListener('click', handleButtonClick);
    });
});

// Form Handling

// Function to validate a form
function validateForm(form) {
    const inputs = form.querySelectorAll('input');
    let isValid = true;
    
    inputs.forEach(input => {
        if (input.required && !input.value) {
            isValid = false;
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    });
    
    return isValid;
}

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    if (validateForm(form)) {
        const formData = new FormData(form);
        console.log('Form Data:', Object.fromEntries(formData.entries()));
        form.reset();
    } else {
        alert('Please fill out all required fields.');
    }
}

// Add event listener to the form with id 'my-form'
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('my-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});

// Example Usage

// Function to display user information
function displayUserInfo(user) {
    const container = document.getElementById('user-info');
    if (container) {
        container.innerHTML = `
            <h2>${user.name}</h2>
            <p>Email: ${user.email}</p>
            <p>Joined: ${formatDate(new Date(user.joinedDate))}</p>
        `;
    }
}

// Fetch and display user information
document.addEventListener('DOMContentLoaded', async () => {
    const user = await fetchData('https://api.example.com/user/1');
    if (user) {
        displayUserInfo(user);
    }
});

// Utility to generate a random color
function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}

// Change background color on button click
function changeBackgroundColor() {
    document.body.style.backgroundColor = getRandomColor();
}

// Add event listener to button with id 'change-color'
document.addEventListener('DOMContentLoaded', () => {
    const colorButton = document.getElementById('change-color');
    if (colorButton) {
        colorButton.addEventListener('click', changeBackgroundColor);
    }
});
