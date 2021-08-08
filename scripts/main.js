// let myHeading = document.querySelector('h1');
// myHeading.textContent = 'Hello world!';

// document.querySelector('html').onclick = function () {
//     alert('痛！')
// }

let myImage = document.querySelector('img');

myImage.onclick = function () {
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'static/images/m2.png') {
        myImage.setAttribute('src', 'static/images/m4.png');
    } else {
        myImage.setAttribute('src', 'static/images/m2.png');
    }
}

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1')

function setUsername() {
    let myName = prompt('请输入您的名字！');
    if (!myName || myName === null) {
        setUsername();
    } else {
        localStorage.setItem('name', myName);
        myHeading.textContent = '欢迎来到测试世界-' + myName;
    }
}

if (!localStorage.getItem('name')) {
    setUsername();
} else {
    let storedname = localStorage.getItem('name');
    myHeading.textContent = '欢迎来到测试世界-' + storedname;
}

myButton.onclick = function () {
    setUsername();
}