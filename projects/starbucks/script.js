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
