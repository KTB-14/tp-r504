import java.net.*;
import java.io.*;

public class ClientTCP3 
{
    public static void main(String[] args) 
    {
        try 
        {
            Socket socket = new Socket("localhost", 2016);
            DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
            DataInputStream dIn = new DataInputStream(socket.getInputStream());

            dOut.writeUTF(args[0]);
            String reponse = dIn.readUTF();
            System.out.println("Message Inversé: " + reponse);

            socket.close();
        }
        catch (Exception e) 
        {
            System.out.println("Erreur !");
        }
    }
}
