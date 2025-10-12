import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientTCP2 
{
    public static void main(String[] args) 
    {
        // Vérifie qu’un argument a été passé (ex: java ClientTCP2 coucou)
        if (args.length < 1) 
        {
            System.out.println("Usage : java ClientTCP2 <message>");
            return;
        }

        try (Socket socket = new Socket("localhost", 2016);
             DataOutputStream dOut = new DataOutputStream(socket.getOutputStream())) 
             {

            // Envoie le premier argument de la ligne de commande
            dOut.writeUTF(args[0]);
            dOut.flush();

            System.out.println("Message envoyé : " + args[0]);

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur client : " + e.getMessage());
        }
    }
}
