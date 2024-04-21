import reflex as rx

class State(rx.State):
    # The images to show.
    img: list[str]
    result: str = "no se ejecuto todavia"
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).
        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename
            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
            # Update the img var.
            self.img.append(file.filename)


def Downloads() -> rx.Component:
    """The main view."""
    return rx.vstack(
        rx.upload(
            rx.vstack(
                rx.button("Select File"),
                rx.text("Drag and drop files here or click to select files"),
            ),
            id="upload1",
            accept = {
            "image/png": [".png"],
            "image/jpeg": [".jpg", ".jpeg"]},
            
        ),
        rx.button(
            "Upload",
            on_click=State.handle_upload(rx.upload_files(upload_id="upload1")),
        ),
        rx.foreach(
            State.img,
            lambda img:rx.image(src=rx.get_upload_url(img))
        ),
        rx.text(State.result)
    )

