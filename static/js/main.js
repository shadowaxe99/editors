document.addEventListener('DOMContentLoaded', function() {
    const videoUploadInput = document.getElementById('video-upload-input');
    const saveButton = document.getElementById('save-button');
    const exportButton = document.getElementById('export-button');
    const videoTimeline = document.getElementById('video-timeline');
    const videoPreview = document.getElementById('video-preview');
    const editPanel = document.getElementById('edit-panel');

    videoUploadInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file && allowedFile(file.name)) {
            const formData = new FormData();
            formData.append('video', file);
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    videoPreview.src = URL.createObjectURL(file);
                    alert(message_names.video_upload_success);
                } else {
                    alert(message_names.video_upload_failure);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert(message_names.video_upload_failure);
            });
        } else {
            alert('Invalid file type.');
        }
    });

    saveButton.addEventListener('click', function() {
        // Logic to save edits
    });

    exportButton.addEventListener('click', function() {
        // Logic to export the edited video
    });

    function allowedFile(filename) {
        const extension = filename.split('.').pop().toLowerCase();
        return ALLOWED_EXTENSIONS.includes(extension);
    }
});