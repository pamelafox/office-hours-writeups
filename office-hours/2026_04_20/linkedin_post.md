In this week's Python + AI Office Hours, we spent most of the session exploring how to extract entities from PDFs using Python.  We compared several approaches:



📄 MarkItDown, PyMuPDF: Two free, open-source Python packages that work well for straightforward documents. We tested both on a complex PDF and they each struggled in different ways. MarkItDown also has an OCR plugin for image descriptions.



We tried those packages out in the entity-extraction demos repo:

https://github.com/Azure-Samples/azure-openai-entity-extraction



📄 Azure Document Intelligence: This cloud service takes things further by extracting figures, tables, and text separately. In our RAG repo, we also added an LLM description step to generate alt-text-style descriptions for each extracted figure. The combination of structured extraction + LLM descriptions gave the richest output for the complex PDF. In the attached screenshot, you can see a page from the PDF next to its extracted chunk.



That code is in the RAG repo, in pdfparser.py and mediadescriber.py :

https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/app/backend/prepdocslib



Remember: Always set up evaluations for your data! Document extraction quality can vary widely depending on the structure and content of your documents.



See the recording and questions here:

https://aka.ms/pythonai/oh/links