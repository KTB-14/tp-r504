import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServeurTCP2 
{
    public static void main(String[] args) 
    {
        try (ServerSocket socketserver = new ServerSocket(2016)) 
        {
            System.out.println("Serveur en attente de connexions...");

            // Le serveur reste actif en permanence
            while (true) 
            {
                try (Socket socket = socketserver.accept();
                     DataInputStream dIn = new DataInputStream(socket.getInputStream())) 
                     {

                    System.out.println("Connexion d’un client");
                    String msg = dIn.readUTF();
                    System.out.println("Message reçu : " + msg);
                } 
                catch (IOException e) 
                {
                    System.err.println("Erreur pendant la communication avec le client : " + e.getMessage());
                }
            }

        } 
        catch (IOException e) 
        {
            System.err.println("Erreur serveur : " + e.getMessage());
        }
    }
}
