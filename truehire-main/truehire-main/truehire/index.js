
// DOM Elements
const menuToggle = document.getElementById('menuToggle');
const navMenu = document.querySelector('.nav-menu');
const exploreBtn = document.getElementById('exploreBtn');
const startChallengeBtn = document.getElementById('startChallengeBtn');

// Mobile menu toggle
menuToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (!target) return;
        
        window.scrollTo({
            top: target.offsetTop - 80, // Offset for fixed navbar
            behavior: 'smooth'
        });
    });
});

// Button click handlers
exploreBtn.addEventListener('click', () => {
    console.log('Get Started button clicked');
    // Navigate to signup page or show modal
    document.querySelector('#benefits').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start',
        inline: 'nearest'
    });
});

startChallengeBtn.addEventListener('click', () => {
    console.log('Get In Touch button clicked');
    // Navigate to challenge start page or show signup modal
    alert('Thank you for your interest! A representative will contact you soon.');
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.boxShadow = 'none';
    }
});

// Animate on scroll
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.benefit-card, .step, .feature-card, .analysis-card');
    
    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementPosition < windowHeight - 100) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
};

// Initial setup for animate on scroll
document.querySelectorAll('.benefit-card, .step, .feature-card, .analysis-card').forEach(element => {
    element.style.opacity = '0';
    element.style.transform = 'translateY(20px)';
    element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
});

window.addEventListener('scroll', animateOnScroll);
window.addEventListener('load', animateOnScroll);

// Form submission (for future integration)
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        console.log('Form submitted');
        // Process form data
    });
});
// Additional functionality can be added here