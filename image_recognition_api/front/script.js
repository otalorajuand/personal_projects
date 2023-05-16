// Get the input element for image upload
const inputElement = document.getElementById("image_upload");

// Add an event listener to the input element to listen for when an image is uploaded
inputElement.addEventListener("change", (event) => {
  // Get the uploaded file
  const file = event.target.files[0];

  // Create a new FileReader object
  const reader = new FileReader();

  // Add an event listener to the FileReader to listen for when the file has finished loading
  reader.addEventListener("load", (event) => {
    // Get the loaded image data as a URL
    const imageDataUrl = event.target.result;

    // Create a new image element and set its source to the loaded image data URL
    const imageElement = document.createElement("img");
    imageElement.src = imageDataUrl;

    // Get the previous image element, if any, and remove it
    const previousImageElement = inputElement.parentNode.querySelector("img");
    if (previousImageElement) {
      previousImageElement.remove();
    }

    // Insert the image element before the input element
    inputElement.parentNode.insertBefore(imageElement, inputElement);
  });

  // Read the uploaded file as a data URL
  reader.readAsDataURL(file);
});
