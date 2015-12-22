package com.example.francisco.atsiaapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.StrictMode;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.JsonReader;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import org.json.*;


import org.json.JSONException;
import org.json.JSONObject;

public class Login extends AppCompatActivity implements View.OnClickListener {

    Button bLogin;
    EditText etUsername, etPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_login);

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();

        StrictMode.setThreadPolicy(policy);

        etUsername = (EditText) findViewById(R.id.etUsername);
        etPassword = (EditText) findViewById(R.id.etPassword);
        bLogin = (Button) findViewById(R.id.bLogin);

        bLogin.setOnClickListener(this);

    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {

            case R.id.bLogin:
                String[] v1 = new String[2];
                String[] v2 = new String[2];

                v1[0] = "usernameL";
                v1[1] = "passwordL";

                String username = etUsername.getText().toString();

                String password = etPassword.getText().toString();

                v2[0] = username;
                v2[1] = password;

                String response = "";
                try {
                    response = Communication.httpGet("/user/", v1, v2);
                } catch (Exception e) {
                    e.printStackTrace();
                }

                String result = "";

                JSONObject obj = null;

                try {
                    obj = new JSONObject(response);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                try {
                    result = obj.getString("result");
                } catch (JSONException e) {
                    // Do something to recover ... or kill the app.
                }


                if(result == "fail")
                    ;
                   // startActivity(new Intent(this, Login.class)) ;
                else if(result == "sucess") {
                    //Intent intent = new Intent(this, forum.class);
                    //intent.putExtra("Nome", username);
                    //startActivity(intent);
                    ;
                }

                break;


        }
    }
}
