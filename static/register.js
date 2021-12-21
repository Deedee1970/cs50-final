var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var passConfirm = document.getElementById("confirmation");
var letter1 = document.getElementById("letter1");
var capital1 = document.getElementById("capital1");
var number1 = document.getElementById("number1");
var length1 = document.getElementById("length1");

// When user clicks on password field, show message box
myInput.onfocus = function () {
    document.getElementById("message").style.display = "block";
};

// when user clicks outside password field, hide message box
myInput.onblur = function () {
    document.getElementById("message").style.display = "none";
};

// When user clicks on password confirmation field, show message box
passConfirm.onfocus = function () {
    document.getElementById("confirm").style.display = "block";
};

// When user clicks outside of password confirmation field, hide message box
passConfirm.onblur = function () {
    document.getElementById("confirm").style.display = "none";
};

// When user starts to type something inside password field
myInput.onkeyup = function () {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    // Validate uppercase letters
    var upperCaseLetters = /[A-Z]/g;
    if (myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if (myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    // Validate length
    if (myInput.value.length >= 6) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }

};

// When user starts to type something inside password field
passConfirm.onkeyup = function () {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if (passConfirm.value.match(lowerCaseLetters)) {
        letter1.classList.remove("invalid");
        letter1.classList.add("valid");
    } else {
        letter1.classList.remove("valid");
        letter1.classList.add("invalid");
    }

    // Validate uppercase letters
    var upperCaseLetters = /[A-Z]/g;
    if (passConfirm.value.match(upperCaseLetters)) {
        capital1.classList.remove("invalid");
        capital1.classList.add("valid");
    } else {
        capital1.classList.remove("valid");
        capital1.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if (passConfirm.value.match(numbers)) {
        number1.classList.remove("invalid");
        number1.classList.add("valid");
    } else {
        number1.classList.remove("valid");
        number1.classList.add("invalid");
    }

    // Validate length
    if (passConfirm.value.length >= 6) {
        length1.classList.remove("invalid");
        length1.classList.add("valid");
    } else {
        length1.classList.remove("valid");
        length1.classList.add("invalid");
    }
};
