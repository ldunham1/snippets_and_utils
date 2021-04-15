from fpdf import FPDF
from PIL import Image


def generate_pdf_from_images(image_list, out_path):
    """
    Generate a PDF file from a list of images.

        >>> image_list = ['C:/image1.png', 'C:/image2.png', 'C:/image3.png']
        >>> output = 'C:/output.pdf'
        >>> generate_pdf_from_images(image_list, output)

    Arguments:
        image_list (list(str)): List of images to create the PDF with.
        out_path (str): Path to write the PDF to.

    Returns:
        (str): Resulting PDF filepath.
    """
    cover = Image.open(image_list[0])

    pdf = FPDF(unit="pt", format=cover.size)

    for image in image_list:
        pdf.add_page()
        pdf.image(image, 0, 0)

    pdf.output(out_path, "F")
    return out_path
