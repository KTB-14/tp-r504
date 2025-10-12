import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientTCP3 
{
    public static void main(String[] args) 
    {
        if (args.length < 1) 
        {
            System.out.println("Usage : java ClientTCP3 <message>");
            return;
        }

        try (Socket socket = new Socket("localhost", 2016);
             DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
             DataInputStream dIn = new DataInputStream(socket.getInputStream())) 
             {

            // Envoyer le message
            dOut.writeUTF(args[0]);
            dOut.flush();

            // Lire la réponse (message inversé)
            String reponse = dIn.readUTF();
            System.out.println("Réponse du serveur : " + reponse);

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur client: " + e.getMessage());
        }
    }
}
