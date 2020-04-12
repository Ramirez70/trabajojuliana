package com.cesde.firebaseacademia;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    EditText nombres, identif;
    Button iniciar;
    TextView registrar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        nombres = findViewById(R.id.etnombres);
        identif = findViewById(R.id.etidentificacion);
        iniciar = findViewById(R.id.btniniciarsesion);
        registrar = findViewById(R.id.tvregistrarse);

        registrar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(getApplicationContext(), Registro.class));
            }
        });
    }
}


