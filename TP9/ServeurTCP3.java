import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServeurTCP3 
{
    public static void main(String[] args) 
    {
        try (ServerSocket socketserver = new ServerSocket(2016)) 
        {
            System.out.println("Serveur en attente de connexions...");

            // Serveur actif en continu
            while (true) 
            {
                try (Socket socket = socketserver.accept();
                     DataInputStream dIn = new DataInputStream(socket.getInputStream());
                     DataOutputStream dOut = new DataOutputStream(socket.getOutputStream())) 
                     {

                    System.out.println("Connexion d’un client");
                    String msg = dIn.readUTF();                 // 1) lire
                    String rev = new StringBuilder(msg).reverse().toString(); // 2) inverser
                    dOut.writeUTF(rev);                         // 3) renvoyer
                    dOut.flush();

                    System.out.println("Reçu: " + msg + "  ->  Renvoyé: " + rev);
                } 
                catch (IOException e) 
                {
                    System.err.println("Erreur client: " + e.getMessage());
                }
            }

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur serveur: " + e.getMessage());
        }
    }
}
