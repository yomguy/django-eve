<?php
/**********************************************************************************
*
*	    This file is part of e-venement.
*
*    e-venement is free software; you can redistribute it and/or modify
*    it under the terms of the GNU General Public License as published by
*    the Free Software Foundation; either version 2 of the License.
*
*    e-venement is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU General Public License for more details.
*
*    You should have received a copy of the GNU General Public License
*    along with e-venement; if not, write to the Free Software
*    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
*
*    Copyright (c) 2006-2015 Baptiste SIMON <baptiste.simon AT e-glop.net>
*    Copyright (c) 2011 Ayoub HIDRI <ayoub.hidri AT gmail.com>
*    Copyright (c) 2006-2015 Libre Informatique [http://www.libre-informatique.fr/]
*
***********************************************************************************/
?>
<?php
    // TDP design
    $this->useClassicTemplateDir(true);
    
    $params = $request->getParameter('member_card');
    if ( $params['created_at']['year'] && $params['created_at']['month'] && $params['created_at']['day'] )
      $params['created_at'] = $params['created_at']['year'].'-'.$params['created_at']['month'].'-'.$params['created_at']['day'];
    else
      $params['created_at'] = date('Y-m-d H:i:s');
    
    $params['expire_at'] = sfConfig::has('project_cards_expiration_delay')
      ? date('Y-m-d H:i:s',strtotime(sfConfig::get('project_cards_expiration_delay'),strtotime($params['created_at'])))
      : (strtotime(date('Y').'-'.sfConfig::get('project_cards_expiration_date')) > strtotime('now')
      ? date('Y').'-'.sfConfig::get('project_cards_expiration_date')
      : (date('Y')+1).'-'.sfConfig::get('project_cards_expiration_date'));
    
    if ( !$request->hasParameter('id') )
      $request->setParameter('id',$params['contact_id']);
    $this->executeShow($request);
    
    $this->member_card_types = Doctrine::getTable('MemberCardType')->createQuery('mct')
      ->leftJoin('mct.Users u')
      ->andWhere('u.id = ?',$this->getUser()->getId())
      ->orderBy('name')
      ->execute();
    
    $this->card = new MemberCardForm();
    $params['active'] = true;
    $this->card->bind($params);
    
    if ( $this->card->isValid() )
    {
      $this->transaction = null;
      if ( !$request->hasParameter('duplicate') )
      {
        $this->transaction = new Transaction;
        $this->transaction->MemberCards[] = $this->card->getObject();
        $this->card->save();
        $this->card = $this->card->getObject();
        
        if ( $this->card->MemberCardType->value > 0 )
        try
        {
          $payment = new Payment;
          if ( intval($pmid = $request->getParameter('payment_method_id')) > 0 )
            $payment->payment_method_id = $pmid;
          else
          {
            $pm = Doctrine::getTable('PaymentMethod')->createQuery('pm')
              ->andWhere('pm.member_card_linked = true')
              ->fetchOne();
            if ( !$pm )
              throw new liMemberCardPaymentException('You need to define a payment method for member cards.');
            $payment->payment_method_id = $pm->id;
          }
          
          $pdtval = 0;
          foreach ( $this->card->BoughtProducts as $bp )
            $pdtval += $bp->value !== NULL ? $bp->value : $bp->getValueFromSchema();
          
          $this->card->Payments[] = $payment;
          $payment->value = -$this->card->MemberCardType->value + $pdtval;
          $this->transaction->Contact = $this->card->Contact;
          $this->transaction->Payments[] = $payment;
          $this->transaction->save();
          $this->card->save(); // for linked products...
        }
      	catch ( liMemberCardPaymentException $e )
      	{
          $this->getContext()->getConfiguration()->loadHelpers('I18N');
          $this->getUser()->setFlash('error', __($e->getMessage()));
          $this->redirect('contact/card?id='.$this->card->contact_id);
        }
        
        // for multiple cards
        for ( $i = 1 ; $i < $request->getParameter('qty', 1) ; $i++ )
        {
          error_log('new card copy');
          $this->card = $this->card->copy();
          if ( isset($payment) )
            $this->card->Payments[] = $payment->copy();
          $this->transaction->MemberCards[] = $this->card;
          $this->card->save();
        }
      }
      else
      {
        $q = Doctrine::getTable('MemberCard')->createQuery('mc')
          ->andWhere('mc.contact_id = ?',$params['contact_id'])
          ->andWhere('mc.member_card_type_id = ?',$params['member_card_type_id'])
          ->andWhere('mc.expire_at > NOW()')
          ->orderBy('mc.id DESC')
          ->limit(1);
        $card = $q->fetchOne();
        
        if ( !$card )
          return 'Params';
        
        // some kind of a hack
        $this->card = $card; // replacing MemberCardForm by MemberCard...
        $this->card->updated_at = NULL;
        //$this->card->name = $params['name'];
        $this->card->save();
      }
      
      $this->setLayout('nude');
      return 'Success';
    }
    else
    {
      $this->payment_methods = Doctrine::getTable('PaymentMethod')->createQuery('pm')
        ->andWhere('pm.member_card_linked = true')
        ->orderBy('pm.name')
        ->execute();
      return 'Params';
    }
