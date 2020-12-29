import sys
sys.dont_write_bytecode = True

import os
import streamlit as st

import Question as Q


# SESSION_FILE_NAME = '.delete.txt'



def on_quit_option_clicked(end):
	# Listener for end session button.
	if end:
		# TO DO - Call closing grid / confirmation view (to be built)
		# os.remove(SESSION_FILE_NAME) 	# Deleting the list of viewed images in this session.
		print("-----------------------")
		pass


def on_go_back_option_clicked(go_back):
	# Listener for go back button.
	# FIX THIS
	if go_back:
		pass	


def on_response_recorded(image_name, value):
	Q.local_viewed.append((image_name, value))
	print("local inside: ", Q.local_viewed)
	Q.button_clicked = True
	# Add item to viewed list
	# with open(SESSION_FILE_NAME, 'a+') as viewed_imgs:
	# viewed_imgs.write(f"{image_name}\t{value}\n")


def change_question(images_directory, unlabeled_images, question):
	# Brings both the new image and the new accept/reject button into the view.
	# with open(SESSION_FILE_NAME, 'r') as f:
	# 	viewed = [tuple(l.strip().split('\t')) for l in f.readlines()]
	# 	print(viewed)
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
	if Q.button_clicked:
		question = st.empty()
	else:
		question = st.beta_container()

	# Create list of filepaths of unlabeled images.(Skip 0th item, store)
	images_directory = "Images/Unlabeled"
	unlabeled_images = os.listdir(path=images_directory)[1:]

	# Create a file that keeps a record of all the viewed files
	# if not os.path.exists(SESSION_FILE_NAME):
	# 	with open(SESSION_FILE_NAME, 'w') as f:
	# 		pass 

	# Call first image and accept/ reject buttons
	change_question(images_directory, unlabeled_images, question)


if __name__ == '__main__':
	main()
