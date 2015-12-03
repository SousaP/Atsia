package com.example.francisco.atsiaapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Window;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class forum extends AppCompatActivity {

    protected TextView title;
    protected ImageView icon;
    protected String username;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_CUSTOM_TITLE);

        setContentView(R.layout.activity_forum);
        //buscar a varaiavel username do login
        username = getIntent().getExtras().getString(username);

        String[] v1 = new String[1];
        String[] v2 = new String[1];

        v1[0] = "nome";
        v2[0] = username;

        String response = "";
        try {
            response = Communication.httpGet("/forum/", v1, v2);
        } catch (Exception e) {
            e.printStackTrace();
        }

        JSONArray jsonArray = null;
        try {
            jsonArray = new JSONArray(response);

            for (int i=0; i<jsonArray.length(); i++) {
                JSONObject item = jsonArray.getJSONObject(i);
                String name = item.getString("nome");
                System.out.println("AQUIII : " + name);
            }

        } catch (JSONException e) {
            // Do something to recover ... or kill the app.
        }

        title = (TextView) findViewById(R.id.title);
        icon  = (ImageView) findViewById(R.id.icon);
    }

}
