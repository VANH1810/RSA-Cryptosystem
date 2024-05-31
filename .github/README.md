# RSA Cryptography
RSA Cryptosystem and RSA Digital Signature Scheme redesigned by [Trần Quốc Việt Anh](https://github.com/VANH1810)

<div id="readme-top"></div>
<!-- TABLE OF CONTENTS -->

## Table of contents

<details>
  <ol>
    <li>
      <a href="#1-general-information">General Information</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#2-parameters">Parameters</a></li>
    <li>
      <a href="#3-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#4-usage">Usage</a></li>
    <li><a href="#5-contributing">Contributing</a></li>
    <li><a href="#6-code-of-conduct">Code of Conduct</a></li>
    <li><a href="#7-funding">Funding</a></li>
    <li><a href="#8-license">License</a></li>
    <li><a href="#9-references">Reference</a></li>
    <li><a href="#10-contact">Contact</a></li>
  </ol>
</details>

<!-- GENAERAL INFORMATION -->
## 1. General Information

RSA Cryptosystem and RSA Digital Signature Scheme

This is an easy-to-use API implementation of RSA Encryption and Decryption, implemented purely in Python. 

Moreover, it helps in creating RSA digital signatures and validating signatures.

You can create and use your own Key curve using the [GenerateKey](../GenerateKey.py)

* Note: The algorithm for generating a large prime key is the Miller–Rabin algorithm - a probabilistic primality test, so there would still be an infinitesimal chance that the key generated is a pseudoprime. SO be careful with it if you plan to apply it in practice.

If you have any way that can accurately check large primes, please contribute to me. We are very welcome
### Built With

[Python](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 2. Parameters
### [RSA Crytosystem](../RSA%20Cryptosystem/)
Keys are written in [Public Key](../RSA%20Cryptosystem/public_key.txt) and [Private Key](../RSA%20Cryptosystem/private_key.txt)

### [RSA Digital Signature Scheme](../RSA%20Digital%20Signature%20Scheme/)
Keys are written in [Public Key](../RSA%20Digital%20Signature%20Scheme/public_key.txt) and [Private Key](../RSA%20Digital%20Signature%20Scheme/private_key.txt)

## 3. Getting Started

### Prerequisites

This repository currently supports Window.
* You have to install Python 3.10.0 or higher. You should install Python in [Python](https://www.python.org/downloads/)

### Installation
1. Clone the repository to local computer

  ```bash
   git clone https://github.com/VANH1810/ElGamal-Cryptosystems-on-Elliptic-Curves.git
  ```
2. Check the Python version
  ```bash
   py --version
  ```
<p align="right">(<a href="#readme-top">Back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## 4. Usage
### [RSA Crytosystem](../RSA%20Cryptosystem/)
#### Encryption
* Please write down the plaintext you want to encrypt [Plain text](../RSA%20Cryptosystem/plaintext.txt)
* To Encryption
  ``` ssh
    py Encrypt.py
    ```
* Then the ciphertext will be written in [Cipher text](../RSA%20Cryptosystem/ciphertext.txt)
#### Decryption
* Please write down the cipher text you want to decrypt [Cipher text](../RSA%20Cryptosystem/ciphertext.txt)

* To Decryption
  ``` ssh
    py Decrypt.py
    ```
* Then the Decrypted Text will be written in [Decrypted Text](../RSA%20Cryptosystem/Decrypted_Message.txt)

### [RSA Digital Signature Scheme](../RSA%20Digital%20Signature%20Scheme/)
#### Sign
* Please write down the message you want to sign in [Message](../RSA%20Digital%20Signature%20Scheme/message.txt)
* To sign
  ``` ssh
      py Sign.py
* Then the signature will be written in [Signature](../RSA%20Digital%20Signature%20Scheme/signature.txt) 

#### Verify
* Please write down the message you want to verify in [Message](../RSA%20Digital%20Signature%20Scheme/message.txt) and the signature in [Signature](../RSA%20Digital%20Signature%20Scheme/signature.txt) 
* To verify
  ``` ssh
      py Verify.py
  ```
* If signature is valid or invalid, the message will be printed to the screen

#### Generate Keys
* To Generate a Key pair
  ``` ssh
    py GenerateKey.py
    ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## 5. Contributing

If you're interested in contributing to My project, we welcome your input. Whether you're a seasoned developer or just starting out, there are many ways you can help improve the project. You can contribute code, documentation, bug reports, or feature requests. To get started, check out the contributing guidelines in the [Contributing](CONTRIBUTING.md) file.

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CODE OF CONDUCT -->
## 6. Code of Conduct
We want everyone who participates in my project to feel welcome and respected. To ensure that happens, we've established a code of conduct that outlines our expectations for behavior. You can read the full text of the code of conduct in the [Code of Conduct](CODE_OF_CONDUCT.md) file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUNDING -->
## 7. Funding
My project is currently self-funded and developed on a volunteer basis. If you're interested in supporting the project financially, we welcome your contributions. You can donate through our/my Open Collective page.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## 8. License
My project is released under the [MIT License](LICENSE.md). This means you're free to use, modify, and distribute the software for any purpose, including commercial use. However, we provide no warranties or guarantees, so use the software at your own risk.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- REFERENCES -->
## 9. References
* [Stinson Paterson_ Cryptography Theory And Practice - CRC Press (2019)](https://www.taylorfrancis.com/books/mono/10.1201/9781315282497/cryptography-douglas-robert-stinson-maura-paterson)
* [RSA - Vietnamese](https://viblo.asia/p/he-ma-hoa-rsa-va-chu-ky-so-6J3ZgkgMZmB)
* [RSA Digital Signature Scheme](https://www.geeksforgeeks.org/rsa-and-digital-signatures/)
* [Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## 10. Contact

* My facebook: Tran Quoc Viet Anh - [quocvietanh.tran](https://www.facebook.com/quocvietanh.tran/) 
* Email: tqvabk24@gmail.com
* My github: [https://github.com/VANH1810](https://github.com/VANH1810)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
