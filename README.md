# arXivQA

## To-do list

- [ ] build a simple PDF search engine that support tags and categories
- [ ] save all PDFs in a separate DB, and provide basic identity checks to avoid duplicates
- [ ] experiment and choose the best vectorstore to store all the data
- [ ] fine-tune the splitting and retrieval aspects
  - [ ] recursivesplitting, contextual compression, MMR, ...
- [ ] PDFs can be added to the store at any time, and the VecDB should update accordingly
- [ ] queries by the user can be filtered on specific documents (maybe via labels?)
  - [ ] try selfquery retrieval
- [ ] build a simple interface with gradio or streamlit
- [ ] bentoml for deploying
- [ ] langsmith for monitoring
  - [ ] design some evaluation tests