from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         # Rendering shirt:
#         self.image("shirtificate.png",x=30, y=30, w=150)
#         # Moving cursor to the right:
#         self.set_font("helvetica", style="B", size=20)
#         # Set text color to white
#         self.set_text_color(255,255,255)
#         # Move cursor and print name in the center of shirt
#         self.cell(200,100, user_name, align="C")
#         # Performing a line break:
#         self.ln(20)


def main():
    # user_name = input("Please Enter your name: ")
    user_name = "Erik the great Solveson"
    pdf = FPDF()
    pdf.add_page()
    # Paste in the shirt with a coordinate for top left and the width
    pdf.image("shirtificate.png", x=5, y=5, w=200)
    # Moving cursor to the right:
    pdf.set_font("helvetica", style="B", size=25)
    # Set text color to white
    pdf.set_text_color(255, 255, 255)
    # Move cursor to the center of the shirt
    pdf.set_xy(60, 45)
    # Print the specified name in the center of the shirt
    pdf.cell(90, 20, user_name, align="C", )
    #set the color of a line
    pdf.set_draw_color(r=255, g=128, b=0)
    #Make a psycedelic square
    for i in range(15):
        pdf.set_fill_color(255 - 15*i)
        pdf.rect(x=80+1*i, y=70+1*i, w=50-2*i, h=50-2*i, style="FD")
    # Save the output to a new pdf
    pdf.output("new-tuto2.pdf")


if __name__ == "__main__":
    main()
