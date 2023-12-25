# Quantum Safe Digital Signature System

This is a Python project that provides a demonstration of signing and verifying documents using Rainbow cryptography. It generates a pair of public and private key files and allows users to sign and verify documents.

Rainbow cryptography is a cryptographic algorithm designed for digital signatures. It is regarded as a post-quantum cryptography system and is a particular kind of multivariate polynomial cryptography. The aim of post-quantum cryptography is to create signature and encryption protocols that are safe in the face of potent quantum computers which are considered to be at the highest standard of computing.

Through the introduction of a Rainbow cryptography-based quantum-resistant digital signature system, I overcame the shortcomings of the current practice. Rainbow cryptography provides long-term security even in a world with potent quantum computers since it is made to withstand quantum attacks. This system will be able to provide digital signatures that are safe against quantum attacks by utilizing the Rainbow scheme, guaranteeing the integrity and validity of documents in the post-quantum future.

Reference paper: https://bit.ly/2vwckRw

## Steps to Run the Project

### Option 1:

1. After downloading the project, navigate to the `cryptovinaigrette` directory.

2. Run the Python script named `cryptovinaigrette.py` using the following command:

   ```bash
   python cryptovinaigrette.py

3. Upon execution, two files will be created in the same directory: Priv.pem (Private Key file) and Pub.pub (Public Key file).

4. You can use these files to sign and verify documents. In the provided code, the files realCat.txt and fakeCat.txt in the test directory are used for signing and verifying.

NOTE: Use the command line argument -v 1 while running the script for useful logs. For detailed logs, use a value >= 2.


### Option 2:

1. After downloading the project, go to the test directory. This directory contains code related to testing.

2. Run the Python script named test.py:

   ```bash
   python test.py

3. Two files, Priv.pem (Private Key file) and Pub.pub (Public Key file), will be created in the same directory.

4. Use these key files to sign and verify documents. In this case, the files realDog.txt and fakeDog.txt in the same directory are used for signing and verifying.


### Option 3:

1.	After downloading the project, go to the project location in the terminal and open the Python interpreter. Now, follow the commands as mentioned in the screenshot below:

<img width="850" height="700" alt="image" src="https://github.com/VinDesiraju/Quantum-Safe-Digitsl-Signature-System/assets/31548669/52cf907d-116d-4a0d-91ac-c8cb685adc74">


### Test Documents:

<img width="387" alt="Screenshot 2023-12-24 at 8 22 14 PM" src="https://github.com/VinDesiraju/Quantum-Safe-Digital-Signature-System/assets/31548669/3bbced7f-45fe-4359-baa1-7bbe485bb566">







