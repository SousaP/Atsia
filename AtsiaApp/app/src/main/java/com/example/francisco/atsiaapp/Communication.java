package com.example.francisco.atsiaapp;

/**
 * Created by Utilizador on 02/12/2015.
 */

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;


public class Communication {
    private final static String USER_AGENT = "Mozilla/5.0";
    static String link = "http://10.0.2.2:8000/api";


    public static String httpPost(String Url, String[] paramName,
                                  String[] paramVal) throws Exception {
        URL obj = new URL(link+Url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        //add reuqest header
        con.setRequestMethod("POST");
        con.setRequestProperty("User-Agent", USER_AGENT);
        con.setRequestProperty("Accept-Language", "en-US,en;q=0.5");


        String urlParameters = "";

        for(int i = 0; i < paramName.length; i++)
        {
            if(i > 0)
                urlParameters += "&";

            urlParameters += paramName[i] + "=" + paramVal[i];

        }
        Charset UTF8_CHARSET = Charset.forName("UTF-8");



        // Send post request
        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.write(urlParameters.getBytes(UTF8_CHARSET));
        wr.flush();
        wr.close();

        int responseCode = con.getResponseCode();
        System.err.println("\nSending 'POST' request to URL : " + link + Url);

        //System.err.println("Post parameters : " + urlParameters);
        //System.err.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        //print result
        System.err.println(response.toString());
        String message =  response.toString();
        System.err.println(message);
        return message;

    }
    public static String httpGet(String Url, String[] paramName,
                                 String[] paramVal) throws Exception {

        //String url = "http://www.google.com/search?q=mkyong";
        String url = Url + "?";
        for(int i = 0; i < paramName.length; i++)
        {
            if(i > 0)
                url += "&";

            url += paramName[i] + "=" +paramVal[i];

        }


        URL obj = new URL(link+url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        // optional default is GET
        con.setRequestMethod("GET");

        //add request header
        con.setRequestProperty("User-Agent", USER_AGENT);



        int responseCode = con.getResponseCode();
        System.out.println("\nSending 'GET' request to URL : " + link+url);
        System.out.println("Response Code : " + responseCode);

        BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        //print result
        System.err.println(response.toString());
        String message =  response.toString();
        //System.err.println(message);
        return message;


    }
}

