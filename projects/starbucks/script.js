/* Smooth scrolling on all navigation links */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

/* Navbar opacity on scroll */

// Get the navbar
const navbar = document.querySelector('.navbar');

let isScrolling;

// Function to adjust the navbar's opacity based on the scroll position
function adjustNavbarOpacity() {
  // Clear the timeout if it's already set
  window.clearTimeout(isScrolling);

  const scrollPosition = window.pageYOffset;
  if (scrollPosition > 0) {
    navbar.style.opacity = 0.5;
  } else {
    navbar.style.opacity = 1;
  }

  // Set a timeout to reset the navbar's opacity after 150 milliseconds
  isScrolling = setTimeout(function() {
    navbar.style.opacity = 1;
  }, 150);
}

// Listen for the scroll event
window.addEventListener('scroll', adjustNavbarOpacity);

/* Hambuger menu (functionality) */
document.querySelector('.hamburger').addEventListener('click', function() {
    document.querySelector('.side-nav').classList.toggle('active');
});

// Close the side nav when a link is clicked
const sideNavLinks = document.querySelectorAll('.side-nav a');

sideNavLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.querySelector('.side-nav').classList.remove('active');
    });
});

/* Background video parallax effect */
window.addEventListener('scroll', function() {
    const parallax = document.querySelector('.background-video');
    let scrollPosition = window.pageYOffset;

    parallax.style.transform = 'translateY(' + scrollPosition * 0.5 + 'px)';
});

/* Background video: Get the video element */
const video = document.querySelector('.background-video');

video.addEventListener('loadedmetadata', function() {
    // Set the currentTime to a random value within the duration of the video
    video.currentTime = Math.random() * video.duration;
    video.play();
});

/* Circle animation (front page) */

// Define the colors that the circles can be
const colors = [
    `hsla(160, 100%, 85%, 0.75)`, // light green
    `hsla(0, 0%, 85%, 0.75)`, // light grey
    `hsla(30, 100%, 85%, 0.75)`, // light brown
    `hsla(0, 0%, 100%, 0.75)` // white
];

// Function to create a circle
function createCircle() {
    const circle = document.createElement('div');
    const size = Math.random() * 400;
    const colorIndex = Math.floor(Math.random() * colors.length);
    const color = colors[colorIndex];
    let content = document.querySelector('.content');
    let posX = 0;
    let posY = Math.random() * (content.offsetHeight - size);

    circle.style.width = `${size}px`;
    circle.style.height = `${size}px`;
    circle.style.background = color;
    circle.style.left = `${posX}px`;
    circle.style.top = `${posY}px`;
    circle.style.opacity = 0; // Start with fully transparent circles

    circle.classList.add('circle');

    // Randomly assign a direction for the circle to move in
    const animationName = Math.random() > 0.5 ? 'moveX' : 'moveY';
    circle.style.animation = `fadeIn 2s forwards, moveX ${Math.random() * 5 + 5}s infinite linear`;

    content.appendChild(circle);

    setTimeout(() => {
        circle.style.animation += `, fadeOut 2s forwards`;
        setTimeout(() => {
            circle.remove();
        }, 3000); // Remove the circle after the fadeOut animation has completed
    }, 3000); // Start the fadeOut animation 5 seconds after the circle is created
}

// Create a circle every second
setInterval(createCircle, 1000);

/* Collapsible menu (corporate) */

// Get all the collapsible elements
const coll = document.getElementsByClassName("collapsible");
let i;

// Add an event listener to each collapsible element
for (i = 0; i < coll.length; i++) {
  // Toggle the active class when a collapsible element is clicked
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    const content = document.querySelector('.corporate');
    // Toggle the max-height property of the content
    if (content.style.maxHeight){
      // Remove the max-height property
      content.style.maxHeight = null;
    } else {
      // Set the max-height to the scroll height of the content
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
// Remove the collapsible menu when the window is resized to a width greater than 768px
window.addEventListener('resize', function() {
  if (window.innerWidth > 768) {
    const content = document.querySelector('.corporate');
    for (i = 0; i < coll.length; i++) {
      coll[i].classList.remove('active');
    }
    content.style.maxHeight = null;
  }
});

/* Random colors cards (products + articles) */

// Get all the articles
const articles = document.querySelectorAll('.article, .product');

// Starbucks color palette
const colorPalette = ['#00704A', '#A18664', '#362415', '#D4E9E2', '#1E4920'];

// Function to get a random color from the color palette
function getRandomColor() {
  const randomIndex = Math.floor(Math.random() * colorPalette.length);
  return colorPalette[randomIndex];
}

// Function to apply a random color to each article
function applyRandomColors() {
  articles.forEach(article => {
    const color = getRandomColor();
    article.style.backgroundColor = color;
    article.style.color = getContrastingColor(color);
  });
}

// Apply a random color to each article every 5 seconds
setInterval(applyRandomColors, 10000);

// Function to calculate the luminance of a color
function getLuminance(color) {
    const rgb = color.slice(1).match(/.{2}/g).map(hex => parseInt(hex, 16));
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2];
  }

  // Function to get a contrasting color
  function getContrastingColor(color) {
    return getLuminance(color) > 128 ? 'black' : 'white';
  }

  // Function to apply a random color to each article
  function applyRandomColors() {
    articles.forEach(article => {
      const color = getRandomColor();
      article.style.backgroundColor = color;
      article.style.color = getContrastingColor(color);
    });
  }
