<h1 align="center"> 🗣 Subject &nbsp;&nbsp;&nbsp;&nbsp;Time-Based One-Time Password</h1>

<br>

<h2>Mandatory Part</h2>

<br>
<p>
  In the language of your choice, you have to implement a program that allows you to store an initial password in file, and that is capable of generating a new one time password every time it is requested.<br>
  You can use any library that facilitates the implementation of the algorithm, as long as it doesn’t do the dirty work, i.e. using a TOTP library is strictly prohibited. Of
  course, you can and should use a library or function that allows you to access system time.<br><br>
  <ul>
    <li>The executable must be named <b>ft_otp</b>
    <li>Your program must take arguments.
    <ul>
      <li>-g: The program receives as argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called <b>ft_otp.key</b>, which is encrypted.
      <li>-k: The program generates a new temporary password based on the key given as argument and prints it on the standard output.
    </ul>
    <li>Your program must use the HOTP algorithm (RFC 4226).
    <li>The generated one-time password must be random and must always contain the same format, i.e. 6 digits.
  </ul>
</p>
<br>
<p>
  You can check if your program is working properly by comparing generated passwords with <b>Oathtool</b> or any tool of your choice.
</p>
<br>

> [!TIP]
> oathtool –totp $(cat key.hex)
