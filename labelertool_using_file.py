
import os
import streamlit as st

import Question as Q
# import Confirm as C



def on_quit_option_clicked(end):
	# Listener for end session button.
	# if end:
	# 	# TO DO - Call closing grid / confirmation view (to be built)
	# 	print("-----------------------")
	# 	viewed = Q.local_viewed
	# 	new_screen = C.Confirm(viewed)
	# 	new_screen.render()
	pass


def on_go_back_option_clicked(go_back):
	# Removes the last item on the list of viewed so the next index is one step back.
	if go_back and len(Q.local_viewed):
		del Q.local_viewed[-1]

		

def on_response_recorded(image_name, value):
	# Appends the image name and value as a tuple to the variable stored in Question
	Q.local_viewed.append((image_name, value))
	print("local inside: ", Q.local_viewed)



def change_question(images_directory, unlabeled_images, question):
	# Brings both the new image and the new accept/reject button into the view.

	print("local: ", Q.local_viewed)
	viewed = Q.local_viewed
	if len(viewed):
		print("inside if")
		if len(viewed) == len(unlabeled_images):
			print("inside if (exit condition)")
			return

		new_index = unlabeled_images.index(viewed[-1][0]) + 1
	else:
		print("inside else")
		new_index = 0

	new_question = Q.Question(unlabeled_images[new_index], on_response_recorded)
	new_question.render(images_directory, question)


def main():
	back_button, quit_button = st.beta_columns(2)

	# Call the back button
	go_back = back_button.button("Go back", key="b")
	on_go_back_option_clicked(go_back)

	# Call the end session button
	end = quit_button.button("End session", key="e")
	on_quit_option_clicked(end)

	# Create a placeholder variable to hold the question view

	question = st.empty()



	# Create list of filepaths of unlabeled images.(Skip 0th item, store)
	images_directory = "Images/Unlabeled"
	unlabeled_images = os.listdir(path=images_directory)[1:]


	# Call first image and accept/ reject buttons
	change_question(images_directory, unlabeled_images, question)


if __name__ == '__main__':
	main()
