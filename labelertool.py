import streamlit as st
from PIL import Image
import os




# Initiate a list - will be filled with tuples (image_name, value)
viewed = []

def render_quit_option():
    # Creates the end session button
    end = st.button("End session", "e")
    on_quit_option_clicked(end)


def on_quit_option_clicked(end):
    # Listener for end session button.
    if end:
        # TO DO - Call closing grid / confirmation view (to be built)
        pass

def render_go_back_option():
    # Creates the go back button
    go_back = st.button("Go back", "b")
    on_go_back_option_clicked(go_back)


def on_go_back_option_clicked(go_back):
    # Listener for go back button.
    if go_back:
        # TO DO - Call closing grid / confirmation view (to be built)
        pass

# Call the end session button 
render_quit_option()

# Call the end session button 
render_go_back_option()

# Create a placeholder variable to hold the question view
question = st.empty()




# Create list of filepaths of unlabeled images.(Skip 0th item, store)
images_directory = "Images/Unlabeled"
unlabeled_images = os.listdir(path=images_directory)[1:]



def on_response_recorded(image_name, value):
    # Add item to viewed list
    viewed.append((image_name, value))
    print(viewed)
    change_question()



class Question:
    image_name = None

    def __init__(self, image_name, callback):
        self.image_name = image_name
        self.callback = callback

    def render_accept_button(self):
        self.accept = st.button("Accept", "a" + self.image_name)
        if self.accept:
            self.on_accept_click()

    def render_reject_button(self):
        self.reject = st.button("Reject", "r" + self.image_name)
        if self.reject:
            self.on_reject_click()

    def on_accept_click(self):
        st.write("Image placed in the positive folder.")
        self.callback(self.image_name, 1)
    
    def on_reject_click(self):
        st.write("Image placed in the negative folder.")
        self.callback(self.image_name, 0)
        
            
    def render(self):
        # # Clear out the old
        # question.empty()

        # Fill in the new
        with question.beta_container():
            # Clear out the old - Doesn't seem to matter if it's here or outside.
            st.empty()

            # Open the image file
            with Image.open(os.path.join(images_directory, self.image_name)) as im:

                # Display the image
                st.image(im, use_column_width=True)

            # # Display the radio button
            # self.render_question_options()

            # Display the reject button
            self.render_reject_button()

            # Display the accept button
            self.render_accept_button()




def change_question():
    # Brings both the new image and the new accept/reject button into the view.
    if len(viewed):
        new_index = unlabeled_images.index(viewed[-1][0]) + 1
    else:
        new_index = 0

    new_question = Question(unlabeled_images[new_index], on_response_recorded)
    new_question.render()



# Call first image and accept/ reject buttons
change_question()
