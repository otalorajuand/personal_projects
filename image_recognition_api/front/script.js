// Get the input element for image upload
const imageUpload = document.getElementById("image_upload");
const responseContainer = document.getElementById("response_container");
const imageContainer = document.getElementById('image_container');

// Add event listener to the file input
imageUpload.addEventListener('change', function(e) {
    // Remove the previously displayed image, if any
    while (imageContainer.firstChild) {
        imageContainer.firstChild.remove();
    }

    // Create a new image element
    const img = document.createElement('img');
    img.style.maxWidth = '100%';
    img.style.maxHeight = '100%';

    // Set the source of the image to the uploaded file
    img.src = URL.createObjectURL(e.target.files[0]);

    // Append the image to the image container
    imageContainer.appendChild(img);

    // Read the uploaded file as a data URL
    const reader = new FileReader();
    reader.readAsDataURL(e.target.files[0]);

    // Create a new FormData object
    const formData = new FormData();

    // Add the file to the FormData object with the name "file"
    formData.append("file", e.target.files[0]);

    // Send the POST request to the API with the FormData as the body
    fetch("http://localhost:8000/api/predict", {
        method: "POST",
        body: formData,
    })
    .then(response => response.text())
    .then(responseText => {
        responseContainer.innerHTML = responseText.replace(/['"]+/g, '');
    })
    .catch(error => {
        console.error(error);
        responseContainer.innerText = "An error occurred: " + error.message;
    });
});
