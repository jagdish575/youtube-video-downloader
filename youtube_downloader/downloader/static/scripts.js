document.addEventListener('DOMContentLoaded', () => {
    const downloadForm = document.getElementById('download-form');

    downloadForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const videoUrl = document.getElementById('video_url').value;
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        console.log("Sending video URL:", videoUrl);

        try {
            const response = await fetch(downloadForm.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ video_url: videoUrl })
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error("Error response:", errorData);
                throw new Error(errorData.error);
            }

            const blob = await response.blob();
            const downloadUrl = window.URL.createObjectURL(blob);
            const a = document.createElement('a');

            const filename = `${videoUrl.split('v=')[1]}.mp4` || 'download.mp4';
            a.href = downloadUrl;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            a.remove();

            window.URL.revokeObjectURL(downloadUrl);
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while downloading the video: ' + error.message);
        }
    });
});
