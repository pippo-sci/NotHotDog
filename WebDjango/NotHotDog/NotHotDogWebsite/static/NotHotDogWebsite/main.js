Dropzone.autoDiscover = false;

const myDropzone = new Dropzone("#my-awesome-dropzone", {
  addRemoveLinks: true,
  url: "upload/",
  maxFiles: 1,
  maxFilesize: 2,  
  acceptedFiles: '.png, .jpg, .jpeg',
  init: function() {
    this.on("addedfile", function(file) {
      if (currentFile) {
        this.removeFile(currentFile);
      }
      currentFile = file;
    });
  }   
  }
);