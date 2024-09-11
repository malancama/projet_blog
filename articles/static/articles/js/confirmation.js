 let deleteUrl = '';

        function openModal(url) {
            deleteUrl = url;
            document.getElementById('confirmationModal').style.display = 'flex';
        }

        document.getElementById('confirmBtn').addEventListener('click', () => {
            window.location.href = deleteUrl;
        });

        document.getElementById('cancelBtn').addEventListener('click', () => {
            document.getElementById('confirmationModal').style.display = 'none';
        });

        window.onclick = function(event) {
            if (event.target == document.getElementById('confirmationModal')) {
                document.getElementById('confirmationModal').style.display = 'none';
            }
        }