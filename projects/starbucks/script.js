document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

document.querySelector('.hamburger').addEventListener('click', function() {
    document.querySelector('.side-nav').classList.toggle('active');
});

const coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    const content = document.querySelector('.corporate');
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

window.addEventListener('resize', function() {
  if (window.innerWidth > 768) {
    const content = document.querySelector('.corporate');
    for (i = 0; i < coll.length; i++) {
      coll[i].classList.remove('active');
    }
    content.style.maxHeight = null;
  }
});


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
