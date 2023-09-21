var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");
function opentab(tabname){
    for(tablink of tablinks){
        tablink.classList.remove("active-link");
    }

    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab")
}
var sitemenu = document.getElementById("sidemenu");

function openmenu(){
    sidemenu.style.top = "0";
}

function closemenu(){
    sidemenu.style.top = "-50%";
}

document.addEventListener("DOMContentLoaded", function() { // Ensure the DOM is fully loaded
    const contactForm = document.getElementById("contact-form");
    if (contactForm) { // Check if the contact form exists on the page
        contactForm.addEventListener("submit", function(event){
            event.preventDefault(); // Prevents the default form submission behavior

            // Fetch form data
            const formData = new FormData(event.target);

            // Send AJAX request
            fetch('/contact', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if(data.message === "Email sent successfully!") {
                    // Display success alert
                    document.getElementById("success-alert").style.display = "block";
                    
                    // Clear the form
                    contactForm.reset();

                    setTimeout(() => {
                        document.getElementById("success-alert").style.display = "none";
                    }, 3000); // Hide the alert after 3 seconds
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});c
