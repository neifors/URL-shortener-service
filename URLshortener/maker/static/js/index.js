function copyURL() {
     /* Get the text field */
     var copyText = document.getElementById("url-result");
   
     /* Select the text field */
     // copyText.select();
     // copyText.setSelectionRange(0, 99999); /* For mobile devices */
   
      /* Copy the text inside the text field */
     // navigator.clipboard.writeText(copyText.value);
     navigator.clipboard.writeText(copyText.textContent);
   
     /* Alert the copied text */
    //  alert("Copied the text: " + copyText.textContent);
   }

