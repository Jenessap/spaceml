import sys
sys.dont_write_bytecode = True

from PIL import Image
import streamlit as st

local_viewed = []
button_clicked = False

class Question:
	def __init__(self, image_name, callback):
		self.image_name = image_name
		self.callback = callback

	# def render_accept_button(self):
	# 	if self.accept:
	# 		self.on_accept_click()

	# def render_reject_button(self):
	# 	if self.reject:
	# 		self.on_reject_click()

	def on_accept_click(self):
		# st.write("Image placed in the positive folder.")
		if self.accept:
			self.callback(self.image_name, 1)

	def on_reject_click(self):
		# st.write("Image placed in the negative folder.")
		if self.reject:
			self.callback(self.image_name, 0)


	def render(self, images_directory, question):
		# Fill in the new
		with question.beta_container():

			# Open the image file
			with Image.open(f"{images_directory}/{self.image_name}") as im:

				# Display the image
				st.image(im, use_column_width=True)

			accept_button, reject_button = st.beta_columns(2)
			self.accept = accept_button.button("Accept", "a" + self.image_name)
			self.reject = reject_button.button("Reject", "r" + self.image_name)

			self.on_reject_click()
			self.on_accept_click()

			# # Display the reject button
			# self.render_reject_button()

			# # Display the accept button
			# self.render_accept_button()

