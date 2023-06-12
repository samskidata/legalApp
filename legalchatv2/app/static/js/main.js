// Modify the JavaScript code to handle file upload and display the link
document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var messageInput = document.getElementById('messageInput').value;
    var fileInput = document.getElementById('fileInput').files[0];
    
    // Create a FormData object to send form data including the file
    var formData = new FormData();
    formData.append('message', messageInput);
    formData.append('file', fileInput);
    
    // Send form data to the server using Fetch API
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response and display the readable link
        var fileLink = data.file_link;
        if (fileLink) {
            var chatArea = document.getElementById('chatArea');
            var linkElement = document.createElement('a');
            linkElement.href = fileLink;
            linkElement.textContent = 'Uploaded Document';
            chatArea.appendChild(linkElement);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
