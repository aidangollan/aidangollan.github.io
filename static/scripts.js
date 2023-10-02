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

document.getElementById("contact-form").addEventListener("submit", function(event){
    event.preventDefault(); // Prevents the form from submitting the traditional way

    var formData = new FormData(this);

    fetch('/contact', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Display the success message by sliding it in
            var successAlert = document.getElementById("success-alert");
            successAlert.style.right = "10px";  // Slide it in
            
            // Slide the success message back out after 3 seconds
            setTimeout(function(){
                successAlert.style.right = "-300px";  // Slide it out
            }, 3000);

            // Clear the form
            document.getElementById("contact-form").reset();
        }
    })
    .catch(error => {
        console.error('There was an error:', error);
    });
});
