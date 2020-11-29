#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph,Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
def generate_report(attachment, title, paragraph):
        report=SimpleDocTemplate(attachment)
        styles=getSampleStyleSheet()
        report_title=Paragraph(title, styles['h1'])
        report_body=Paragraph(paragraph)
        spacer1=Spacer(5,10)
        return report.build([report_title,spacer1,report_body])
if '__name__'=='__main__':
        generate_report()
